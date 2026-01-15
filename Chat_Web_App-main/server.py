from myapp import create_app
from myapp.database import db, Message, ChatMessage
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask import request   # ← we need this
from datetime import datetime
import time

app, socket = create_app()   # socket is your SocketIO instance

# ─── ONLINE STATUS TRACKING ───────────────────────────────────────────────
last_seen = {}           # username → last activity datetime
sid_to_username = {}     # sid → username

def mark_online(username):
    if not username:
        return
    last_seen[username] = datetime.utcnow()
    # We broadcast to everyone
    emit('user_status', {
        'username': username,
        'online': True,
        'last_seen': None
    }, broadcast=True, include_self=False)

def mark_offline(username):
    if username in last_seen:
        last_seen_time = last_seen[username].isoformat()
        emit('user_status', {
            'username': username,
            'online': False,
            'last_seen': last_seen_time
        }, broadcast=True, include_self=False)
        last_seen.pop(username, None)

# ─── SOCKET HANDLERS ──────────────────────────────────────────────────────

@socket.on('connect')
def handle_connect():
    print('Client connected')

@socket.on('disconnect')
def handle_disconnect():
    sid = request.sid
    username = sid_to_username.pop(sid, None)
    if username:
        print(f'User disconnected (offline soon): {username}')

@socket.on('register')
def handle_register(data):
    username = data.get('username')
    if username:
        sid_to_username[request.sid] = username
        mark_online(username)
        print(f'Registered: {username}')

@socket.on('join-chat')
def join_private_chat(data):
    room = data.get("rid")
    if room:
        join_room(room)
        emit("joined-chat", {"msg": f"Joined room {room}"}, room=room, include_self=False)

@socket.on('outgoing')
def chatting_event(json):
    room_id = json.get("rid")
    timestamp = json.get("timestamp")
    message = json.get("message")
    sender_id = json.get("sender_id")
    sender_username = json.get("sender_username")

    if sender_username:
        mark_online(sender_username)

    message_entry = Message.query.filter_by(room_id=room_id).first()
    if not message_entry:
        return

    chat_message = ChatMessage(
        content=message,
        timestamp=str(timestamp),
        sender_id=sender_id,
        sender_username=sender_username,
        room_id=room_id,
    )

    try:
        message_entry.messages.append(chat_message)
        db.session.add(chat_message)
        db.session.commit()
    except Exception as e:
        print("Save error:", str(e))
        db.session.rollback()
        return

    emit("message", json, room=room_id, include_self=False)

# Background offline detection
def check_offline():
    while True:
        time.sleep(45)
        now = datetime.utcnow()
        to_remove = []
        for u, last in list(last_seen.items()):
            if (now - last).total_seconds() > 120:  # 2 min timeout
                mark_offline(u)
                to_remove.append(u)
        for u in to_remove:
            last_seen.pop(u, None)

socket.start_background_task(check_offline)

if __name__ == "__main__":
    socket.run(app, allow_unsafe_werkzeug=True, debug=True)
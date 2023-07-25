import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
# from .Game import game
from .ChessQueue import chessQueue
from .Games import gameDict


class ChessConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name='players'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        request = json.loads(text_data)
        # print(gameDict.games)
        if request['type'] == "make_move":
            message = request['message']
            game = gameDict.games[request['game_id']]
            game.run(request)
            # print(self.scope)
            # print(self.room_group_name)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'text': "text2",
                    'message': message,
                    'game_response': game.response
                }
            )
        if request['type'] == "start_game":
            self.room_group_name = request['game_id']

            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )

    def chat_message(self, event):
        # print(game.get_response())
        self.send(text_data=json.dumps({
            'type': 'chat',
            'text': event['text'],
            'message': event['message'],
            'response': event['game_response']
        }))


class FindGameConsumer(WebsocketConsumer):
    def connect(self):
        # print(self.scope['user'])
        self.room_group_name = 'users'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_add)(
            "users_in_queue",
            self.channel_name
        )
        request = json.loads(text_data)
        player = request['user']
        # print(gameDict.games)
        # chessQueue.add_player(player)
        if chessQueue.can_find_game():
            # gamename = chessQueue.create_game_name(player)
            # print(gamename)
            game1 = chessQueue.create_game(player)
            game_id = game1.gamedb.id
            gameDict.add_game(game_id, game1)
            # print(chessQueue.players)
            async_to_sync(self.channel_layer.group_send)(
                "users_in_queue",
                {
                    'type': 'start_game',
                    'text': "text2",
                    'game_id': game_id,
                }
            )
        else:
            chessQueue.add_player(player)
            print(chessQueue.players)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'queue',
                    'text': "text2",
                }
            )

    def start_game(self, event):
        self.send(text_data=json.dumps({
            'type': 'start_game',
            'text': event['text'],
            'game_id': event['game_id'],
        }))

    def queue(self, event):
        self.send(text_data=json.dumps({
            'type': 'queue',
            'text': event['text'],
        }))

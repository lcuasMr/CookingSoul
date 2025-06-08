from models.user import User


class UserMapper:
    @staticmethod
    def map(json_data):
        id = json_data.get('id')
        username = json_data.get('nombre')
        email = json_data.get('email')
        password = json_data.get('password')
        posts = json_data.get('posts', [])
        return User(id, username, email, password, posts)

    @staticmethod
    def reverse_map(usuario):
        return {
            'id': usuario.id,
            'nombre': usuario.username,
            'email': usuario.email,
            'password': usuario.password,
            'posts': usuario.posts
        }
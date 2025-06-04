from models.user import User


class UsuarioMapper:
    @staticmethod
    def map(json_data):
        id = json_data.get('id')
        username = json_data.get('nombre')
        email = json_data.get('email')
        password = json_data.get('password')
        return User(id, username, email, password)

    @staticmethod
    def reverse_map(usuario):
        return {
            'id': usuario.id,
            'nombre': usuario.username,
            'email': usuario.email,
            'password': usuario.password
        }
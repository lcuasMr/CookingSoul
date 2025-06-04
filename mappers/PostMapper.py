from models.post import Post 

class PostMapper:
    @staticmethod
    def map(json_data):
        id=json_data.get("id")
        type=json_data.get("type")
        content=json_data.get("content")
        return Post(id, type, content)

    @staticmethod
    def reverse_map(post: Post):
        return {
            "id": post.id,
            "type": post.type,
            "content": post.content,
        }
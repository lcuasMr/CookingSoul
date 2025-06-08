from models.post import Post 

class PostMapper:
    @staticmethod
    def map(json_data):
        id=json_data.get("id")
        user_id=json_data.get("user_id")
        type=json_data.get("type")
        description=json_data.get("description")
        recipie_id=json_data.get("recipie_id")
        likes=json_data.get("likes", 0)
        return Post(id, user_id, type, description, recipie_id, likes)

    @staticmethod
    def reverse_map(post: Post):
        return {
            "id": post.id,
            "user_id": post.user_id,
            "type": post.content_type,
            "description": post.description,
            "recipie_id": post.recipie_id,
            "likes": post.likes
        }
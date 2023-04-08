from django.db import models

# Defines a Post object in the blog.
class BlogPost(models.Model):
    """
        Args:
        - content (str): The text content of the post
    """
    content = models.TextField()
    
    def __str__(self):
        return str(self.pk)
    



from django.db import models
import string
import random

def generate_unique_room_code():
    length = 6
    
    while True:
        # generate a random code with uppercase ascii characters with length of code
        code = "".join(random.choices(string.ascii_uppercase, k=length))

        # compares with database to see if there are no other rooms with the generated code
        if Room.objects.filter(code=code).count() == 0:
            break
    
    return code



# Create your models here.
class Room(models.Model):
    # information we want to store in each music room
    code = models.CharField(max_length=8, default="password", unique=True)  # stores the room code
    host = models.CharField(max_length=50, unique=True)  # stores the host id
    guest_can_pause = models.BooleanField(null=False, default=False)  # stores whether a room guest can pause the music
    votes_to_skip = models.IntegerField(null=False, default=1)  # stores the number of votes required to skip the song
    created_at = models.DateTimeField(auto_now_add=True)  # automatically adds the date and time to the created_at variable


import random
import math
from itertools import combinations
from Queue import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # Add users
        # for i in range(numUsers):
        #     self.addUser(i)
        # # Create friendships
        # for j in range(numUsers):
        #     for k in range(random.randint(0, avgFriendships+1)):
        #         r_int = random.randint(1, numUsers)
        #         print("r_int", r_int)
        #         self.addFriendship(j, r_int)

        # Redone code
        # adds all users based on the parameter above
        for i in range(numUsers):
            self.addUser(i)
        all_friends = list(combinations(range(1, len(self.users)+1), avgFriendships))
        random.shuffle(all_friends)
        actual = all_friends[:numUsers]
        # print("ACTUAL" , actual)
        for friend in actual:
            # print("Friend 1:", friend[0], "Friend 2:", friend[1])
            self.addFriendship(friend[0], friend[1])
        # print(all_friends)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([userID])
        while q.len() is not 0:
            n = q.dequeue()
            node = n[-1]
            if node not in visited:
                visited[node] = n
            for i in self.friendships[node]:
                if i not in visited:
                    next_path = list(n)
                    next_path.append(i)
                    q.enqueue(next_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

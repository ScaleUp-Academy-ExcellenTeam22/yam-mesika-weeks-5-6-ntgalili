import math


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username: str, number_of_messages: int = None) -> list:
        """
        The function returns the number of messages requested from the user's mailbox.
        :param username: The name of the user that requesting his messages.
        :param number_of_messages: Number of messages requested.
        :return: List of the requested messages.
        :raises KeyError: if the username does not exist.
        """
        to_return = self.boxes[username][:number_of_messages]
        del self.boxes[username][number_of_messages:]
        return to_return

    def search_inbox(self, username: str, to_search: str) -> list:
        """
        The function search str in user box.
        :param username: The searcher's name.
        :param to_search: The str to search.
        :return: The messages that contain the string in their body or their title.
         :raises KeyError: if the username does not exist.
        """
        user_box = self.boxes[username]
        return [message for message in user_box if (to_search in message['body'] or to_search in message['sender'])]




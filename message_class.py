
class Message:
    """
    Message class, the class represents a virtual message.

    :ivar id: message id.
    :ivar sender: The sender's name.
    :ivar body: The message content.
    :ivar is_read: Indicates whether the message was read.
    """
    def __init__(self, message_id: int, message_sender: str, message_body: str, is_read: bool = False):
        """
        c-tor for message class.
        :param message_id: message id.
        :param message_sender: The sender's name.
        :param message_body: The message content.
        :param is_read:  Indicates whether the message was read.
        """
        self.id = message_id
        self.sender = message_sender
        self.body = message_body
        self.is_read = is_read

    def __str__(self):
        """
        Convert the message to str.
        :return:  str of the message.
        """
        return f"message id: {str(self.id)} message sender: {self.sender} \n {self.body}"

    def __len__(self):
        """
        Calculates the message size.
        :return: The message size.
        """
        return len(self.body)


class PostOffice:
    """
    A Post Office class. Allows users to message each other.

    :ivar message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames: list):
        """
        c-tor for message class.
        :param usernames: List of users name.
        """
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """
        Send a message to a recipient.

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
        message = Message(self.message_id, sender, message_body)
        if urgent:
            user_box.insert(0, message)
        else:
            user_box.append(message)
        return self.message_id

    def read_inbox(self, username: str, number_of_messages: int = None) -> list:
        """
        The function returns the number of messages requested from the user's mailbox.
        :param username: The name of the user that requesting his messages.
        :param number_of_messages: Number of messages requested.
        :return: List of the requested messages.
        :raises KeyError: if the username does not exist.
        """
        to_return = list(filter(lambda m: not m.is_read, self.boxes[username]))[:number_of_messages]
        for message in to_return:
            message.is_read = True
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
        return [message for message in user_box if (to_search in str(message))]

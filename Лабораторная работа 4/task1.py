if __name__ == "__main__":
    # Write your solution here
    pass

from datetime import datetime
from typing import List


class SocialNetwork:
    """
    Abstract social network
    """

    def __init__(self, name: str, founders: List[str], foundation_date: datetime.date, servers: List[str],
                 number_of_users: int) -> None:
        self.name = name
        self.founders = founders
        self.foundation_name = foundation_date
        self.servers = servers
        self.number_of_users = number_of_users

    def __str__(self) -> str:
        """
        social network string representation
        :return: str
        """
        return f"Social network name: {self.name}, " \
               f"founders: {self.founders}, current number of users: {self.number_of_users}"

    def __repr__(self) -> str:
        """
        social network object representation
        :return: str
        """
        return f"SocialNetwork(name={self.name}, founders={self.founders}, foundation_date={self.foundation_name}, " \
               f"servers={self.servers}, number_of_users={self.number_of_users})"

    def add_new_user(self) -> None:
        """
        Add new user to network
        :return: None
        """
        self.number_of_users += 1


class Facebook(SocialNetwork):
    """
    Facebook network
    """

    def __init__(self, name: str, founders: List[str], foundation_date: datetime.date, servers: List[str],
                 number_of_users: int, number_of_instagram_users: int) -> None:
        super().__init__(name, founders, foundation_date, servers, number_of_users)
        self.number_of_instagram_users = number_of_instagram_users
        self.__secret_data = "SECRET FACEBOOK DATA"

    def __get_users_statistic(self) -> int:
        """
        get facebook and instagram users
        статистика внутри класса для внутринних алгоритмов Facebook
        :return: int
        """
        return self.number_of_users + self.number_of_instagram_users

    def __str__(self) -> str:
        """
        facebook string representation
        :return: str
        """
        return f"Facebook: founders-{self.founders}, facebook users-{self.number_of_users}, " \
               f"number of instagram users-{self.number_of_instagram_users}"

    def add_new_user(self) -> None:
        """
        регистрация в facebook и в instagram одновременно
        :return: None
        """
        self.number_of_users += 1
        self.number_of_instagram_users += 1


class VK(SocialNetwork):
    """
    VK network
    """

    def __init__(self, name: str, founders: List[str], foundation_date: datetime.date, servers: List[str],
                 number_of_users: int, twitter_users: int) -> None:
        super().__init__(name, founders, foundation_date, servers, number_of_users)
        self.twitter_users = twitter_users
        self.__secret_data = "SECRET VK DATA"

    def __str__(self) -> str:
        """
        vk string representation
        :return: str
        """
        return f"VK: founders-{self.founders}, vk users-{self.number_of_users}, " \
               f"twitter users-{self.twitter_users}"

    def __iter_through_secret_data(self) -> None:
        """
        просмотр этой информации должен быть доступен только внутри класса
        :return: None
        """
        for data in self.__secret_data:
            print(data)

    def add_new_user(self) -> None:
        """
        Регистрация происходит сразу и в vk и в twitter
        :return: None
        """
        self.number_of_users += 1
        self.twitter_users += 1

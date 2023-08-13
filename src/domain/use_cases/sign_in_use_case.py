from abc import ABC, abstractclassmethod

from result import Result

from src.domain.models.message_model import MessageModel
from src.domain.parameters.sign_in_parameter import SignInParameter
from src.domain.models.autentication_model import AuthenticationModel
from src.domain.repositories.authentication_repository import AuthenticationRepository

class SignInUseCase(ABC):

    @abstractclassmethod
    async def run(self, parameter: SignInParameter) -> Result[MessageModel, AuthenticationModel]:
        pass

class SignInUseCaseImpl(SignInUseCase):
    def __init__(self, repository: AuthenticationRepository) -> None:
        self.__repository = repository

    async def run(self, parameter: SignInParameter) -> Result[MessageModel, AuthenticationModel]:
        return await self.__repository.sign_in(parameter)

from fastapi import status, FastAPI, Response

from src.domain.use_cases.sign_in_use_case import SignInUseCaseImpl
from src.external.network.clients.http_client import HttpClientImpl
from src.domain.parameters.sign_in_parameter import SignInParameter
from src.domain.repositories.authentication_repository import AuthenticationRepositoryImpl

from src.data.datasources.remote.remote_authentication_datasource_impl import (
    RemoteAuthenticationDatasourceImpl
)

app = FastAPI(title="King's Cross")

client = HttpClientImpl()
datasource = RemoteAuthenticationDatasourceImpl(client)
repository = AuthenticationRepositoryImpl(datasource)
use_case = SignInUseCaseImpl(repository)

@app.post("/")
async def sign_in(parameter: SignInParameter, response: Response):
    data = await use_case.run(parameter)

    if data.is_err():
        response.status_code = status.HTTP_400_BAD_REQUEST
        return data.err()
    else:
        response.status_code = status.HTTP_200_OK
        return data.ok()

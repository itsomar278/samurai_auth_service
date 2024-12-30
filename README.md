# Authentication Service

[System Overview Documentation](https://daffodil-throne-f06.notion.site/SamurAI-System-Overview-14c82c979e8480348029ec1cc43e9249?pvs=4)

This service manages user authentication and authorization for the SamurAI system, providing secure access control through JWT tokens.

## System Overview
![System Architecture](https://github.com/itsomar278/samurai_video_service/blob/main/ezgif-4-77c29e34de%20(1).gif)

## Features

- User registration and login
- JWT-based authentication with access and refresh tokens
- Token refresh mechanism
- Token blacklisting for secure logout
- Custom user model with email-based authentication

## Installation

1. Clone the repository:
```bash
git clone https://github.com/itsomar278/samurai_auth_service
cd samurai_auth_service
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file with:
```env
JWT_SECRET_KEY=
DJANGO_SECRET_KEY=
MYSQL_DB=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=
MYSQL_PORT=
```

## API Endpoints

### Authentication
- `POST /api/register/`: Register new user
  - Body: `{email, password, first_name, last_name}`

- `POST /api/login/`: Login user
  - Body: `{email, password}`
  - Returns: Access and refresh tokens

- `POST /api/logout/`: Logout user
  - Requires: Valid refresh token
  - Blacklists the refresh token

- `POST /api/token/refresh/`: Refresh access token
  - Body: `{refresh}`
  - Returns: New access token

- `POST /api/token/verify/`: Verify token validity
  - Body: `{token}`

## Related Services

- Transclation Service: [samurai_video_service](https://github.com/itsomar278/samurai_video_service)
- API Gateway: [samurai_api_gateway](https://github.com/itsomar278/samurai_api_gateway)
- LLM Interaction Service: [samurai_LLM_interaction](https://github.com/itsomar278/samurai_LLM_interaction)

## Security Notes

- Uses JWT for stateless authentication
- Implements token refresh mechanism
- Supports secure logout through token blacklisting
- Email-based authentication with custom user model
- Password hashing using Django's default hasher

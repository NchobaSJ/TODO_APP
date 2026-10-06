from app.core.security import fastapi_users

# Anyone logged in + active
current_active_user = fastapi_users.current_user(active=True)

# Anyone logged in + active + superuser (for admin routes)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

# Optional: user is None if not logged in
optional_current_user = fastapi_users.current_user(active=True, optional=True)
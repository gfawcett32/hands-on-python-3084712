import os # the library provides a way to interact with the operating system's functionality

DEVELOPMENT = "development" # multiple production environment variables are defined
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", LOCAL)# os.environ is a dictionary like object that provides access to the environment variables of the OS.
# the get method return the value of the variable ENV_NAME or if not found, return default value DEVELOPMENT
if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment") # exception handlig meaning the environment can't be found

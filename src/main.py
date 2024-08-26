import logging
import container

# Configure logging
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)


def main():
    repo_data = container.get_repo_data()
    repo_data.save_repo_stats()


if __name__ == "__main__":
    main()

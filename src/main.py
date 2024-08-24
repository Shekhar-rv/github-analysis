import logging
import container

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    repo_data = container.get_repo_data()
    repo_data.save_repo_stats()


if __name__ == "__main__":
    main()

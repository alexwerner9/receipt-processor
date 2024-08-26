## Receipt Processor Challenge

This is the implementation of the challenge [here](https://github.com/fetch-rewards/receipt-processor-challenge).

## Setup instructions

1. Clone this repository: `git clone git@github.com:alexwerner9/receipt-processor.git` or without SSH with `git clone https://github.com/alexwerner9/receipt-processor.git`
2. Enter into the cloned repository: `cd receipt-processor`
3. Create and run the Docker image and container: `docker compose up`. If `docker compose` is not in your Docker installation, use the command `docker build -t receipt-processor . && docker run -p 8000:8000 --name receipt-processor receipt-processor`
4. The server is running on port `8000`. For Swagger documentation and queries go to http://localhost:8000/apidocs.
5. (Optional) to run the unit tests, enter into the Docker container with `docker exec -it receipt-processor bash` and run `PYTHONPATH=. pytest`

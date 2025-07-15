# Smart Notes

Smart Notes is a study aid that automatically summarizes images of book pages. Images are captured, processed to extract text, and summarized, with the results saved to a Notion page specified by the user.

## Features

- Capture images of book pages
- Automatic text extraction from images (OCR)
- Content summarization using LLMs
- Save summaries to a Notion page

## Architecture

This project uses a backend exposed via n8n, which orchestrates the workflow. When an image is submitted, n8n invokes endpoints hosted on Azure Container Apps. These endpoints perform OCR on the provided image to extract text, and then use a Large Language Model (LLM) to generate a summary of the extracted content. The final summary is then saved to the user's Notion page via the Notion API.

## Project Setup

### 1. n8n Workflow Configuration

1. Access your n8n instance at:  
    `http://<home_server>:5678/projects/F0u3PIPriMdsGvXi/workflows`
2. Configure the workflow following the instructions in the interface.
3. Enter your Notion credentials and other required parameters.

### 2. Docker Setup

Make sure Docker is installed on your system.

1. Clone this repository:
    ```bash
    git clone https://github.com/<your-username>/smart-notes.git
    cd smart-notes
    ```
2. Create a `.env` file with the required variables (see `.env.example` for reference).
3. Start the services with Docker Compose:
    ```bash
    docker-compose up -d
    ```
4. Check that the containers are running:
    ```bash
    docker ps
    ```

## Notes

- Ensure your Notion page is accessible via the API and the token is valid.
- Customize the n8n workflow to fit your needs.

## License

This project is distributed under the MIT license.

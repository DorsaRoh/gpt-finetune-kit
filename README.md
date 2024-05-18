# GPT-FineTune-Kit

A super easy tool to fine-tune GPT models using the OpenAI API with a simple Flask backend and React frontend.

### What's Fine-Tuning?

Fine-tuning is training a pre-trained AI model (like GPT) on a specific dataset to adapt it to particular needs or improve its performance on certain types of tasks!


## How it Works

In the `server` folder:
    
- The data to fine-tune the model is located in `data/data.jsonl`
<i><br>(see finetune.py for the fine-tuning code)</br></i>
- The fine-tuned model will be identified with an ID, which will be stored in `model_id.txt`

<i>Note: You will find sample data/prompts in data.jsonl</i>

### API Key Requirement

- You will need an OpenAI API key to use this toolkit.
- Add your OpenAI API key to a `.env` file in the `server` directory:

  ```plaintext
  OPENAI_API_KEY=your_openai_api_key_here
    ```
    
## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/gpt-finetune-kit.git
   cd gpt-finetune-kit
    ```


2. **Navigate to the 'server' directory**
    ```bash
    cd server
    pip install -r requirements.txt
    ```

2. **Insert the desired data and prompts in data/data.jsonl**

3. **Fine-tune model**
    ```bash
    python finetune.py
    ```

4. **Start the backend server to initiate the backend**
    ```bash
    python server.py
    ```
    <i>**The backend is now at http://localhost:8080/api/home**</i>


5. **Set up the frontend:**
Open a new terminal and navigate to the client directory
    ```bash
    cd ../client
    npm install
    npm run dev
    ```

    **<i>The frontend is now accessible at http://localhost:3000</i>**


Note: Please check your OpenAI projects dashboard to confirm the status of your fine-tuning jobs. If a job fails, it is likely due to improperly formatted or insufficient data.

Happy fine-tuning!
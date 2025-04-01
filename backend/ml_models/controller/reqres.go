package main

// THIS IS A DEMO SCRIPT
// HAVE TO MODIFY ACCORDINGLY

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type OllamaRequest struct {
	Model  string `json:"model"`
	Prompt string `json:"prompt"`
}

type OllamaResponse struct {
	Response string `json:"response"`
	Done     bool   `json:"done"`
}

func main() {
	url := "http://your-ec2-ip-or-alb-dns:11434/api/generate" // Replace with your URL

	requestBody, err := json.Marshal(OllamaRequest{
		Model:  "my_model", // Replace with your model name
		Prompt: "Hello, Ollama!",
	})
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	resp, err := http.Post(url, "application/json", bytes.NewBuffer(requestBody))
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body) // Corrected line
	if err != nil {
		fmt.Println("Error reading response:", err)
		return
	}

	var response OllamaResponse
	err = json.Unmarshal(body, &response)
	if err != nil {
		fmt.Println("Error unmarshaling JSON:", err)
		return
	}

	fmt.Println("Response:", response.Response)
}

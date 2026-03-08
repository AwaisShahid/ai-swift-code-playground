# AI Code Review Playground

AI Code Review Playground is a lightweight prototype that reviews short code snippets and provides quick feedback before human code review.

The tool analyzes code for **readability, structure, maintainability, and potential issues**, then returns:

- **Three suggested improvements**
- **One positive observation**

The goal is to demonstrate how an AI assistant could act as a **pre-review layer**, helping developers catch common issues before submitting pull requests.

---

## Overview

Code reviews are an essential part of modern software development. However, many reviews focus on repetitive issues such as:

- Unsafe patterns
- Weak error handling
- Missing validation
- Readability improvements

AI Code Review Playground demonstrates how automated analysis could assist developers by identifying potential improvements before a human reviewer analyzes the code.

This reduces reviewer workload and improves overall code quality.

---

## Features

- Paste any code snippet
- Automatic language detection
- Syntax highlighted code preview
- Dynamic pattern-based analysis
- Structured feedback with improvements and a positive note
- Lightweight prototype with minimal dependencies

---

## Demo Example

### Input (Swift)

```swift
func fetchUsers(completion: @escaping ([User]?, Error?) -> Void) {

    let url = URL(string: "https://api.example.com/users")!

    URLSession.shared.dataTask(with: url) { data, response, error in

        if error != nil {
            completion(nil, error)
            return
        }

        if let data = data {
            let users = try? JSONDecoder().decode([User].self, from: data)
            completion(users, nil)
        }

    }.resume()
}
```

Example Output

Detected Language: Swift

Improvements

Potentially unsafe expression url! detected. Consider validating the value before usage.

Error handling pattern try? may suppress decoding failures.

Network call dataTask detected. Ensure response validation before processing results.

Positive Note

The function structure is clearly defined and uses asynchronous completion handlers appropriately.

Tech Stack

Python

Streamlit

How to Run

Install dependencies:
pip install streamlit

Run the application:
streamlit run app.py

How It Works

The prototype performs lightweight pattern detection on the provided code snippet.
It identifies common development patterns and generates contextual feedback based on detected elements.

Examples of analyzed patterns include:

Unsafe value usage

Silent error handling

Network operations

Function size and structure

Documentation presence

This approach simulates how an AI assistant might provide early feedback before human code review.

Potential Real-World Use

A system like this could be integrated into:

GitHub Pull Request checks

CI/CD pipelines

IDE extensions

Developer productivity tools

By providing automated pre-review feedback, teams could reduce review time and improve code quality.

Dataset

No external dataset was required.
Dummy Swift and Python code snippets were used for testing.

Author

Prototype created by Awais Shahid.




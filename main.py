import openai
import requests

# Set up your API keys
openai.api_key = 'OPENAI_API_KEY'
serpapi_api_key = 'SERPAPI_API_KEY'


def generate_query(input_text):
    # Use OpenAI API to generate a relevant search query
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Generate a search query based on this text: {input_text}"}
        ]
    )
    query = response['choices'][0]['message']['content']
    return query.strip()


def get_links(query):
    # Use SerpAPI to fetch Google search results
    search_url = "https://serpapi.com/search"
    params = {
        "q": query,
        "engine": "google",
        "api_key": serpapi_api_key
    }

    response = requests.get(search_url, params=params)
    response.raise_for_status()
    search_results = response.json()

    links = []
    for result in search_results.get("organic_results", []):
        links.append(result["link"])
    return links


def main(input_text):
    query = generate_query(input_text)
    print(f"Generated Query: {query}")

    links = get_links(query)
    print("Relevant Links:")
    for link in links:
        print(link)


if __name__ == "__main__":
    user_input = input("Enter the text to find relevant resources: ")
    main(user_input)

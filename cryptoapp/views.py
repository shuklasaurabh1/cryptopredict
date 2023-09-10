from django.core.paginator import Paginator
from django.shortcuts import render
import requests
from datetime import datetime


def home(request):
    return render(request, 'home.html')

def cryptocurrency_list(request):
    # Define the base URL of the CoinGecko API for fetching the list of cryptocurrencies
    base_url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 100,
    'page': 1,
    'sparkline': False,
    'locale': 'en'
}   

    try:
        # Send a GET request to fetch the list of cryptocurrency IDs
        response = requests.get(base_url, params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            crypto_data = response.json()
            crypto_ids = [crypto["id"] for crypto in crypto_data]

            # Create a Paginator instance with a fixed number of items per page (e.g., 10 items per page)
            paginator = Paginator(crypto_ids, 10)  # Change 10 to the desired number of items per page

            # Get the current page number from the request (default to page 1)
            page_number = request.GET.get('page', 1)

            # Get the page object for the current page
            page = paginator.get_page(page_number)

            # Render the page with the paginated list of IDs
            return render(request, 'cryptocurrency_list.html', {'page': page})

        else:
            return render(request, 'error.html', {'error_message': f"Failed to fetch data. Status code: {response.status_code}"})
    except Exception as e:
        return render(request, 'error.html', {'error_message': f"An error occurred: {str(e)}"})


def cryptocurrency_detail(request, cryptocurrency_id):
    # Define the base URL of the CoinGecko API for fetching cryptocurrency details
    base_url = f"https://api.coingecko.com/api/v3/coins/{cryptocurrency_id}"

    try:
        # Send a GET request to fetch the cryptocurrency details
        response = requests.get(base_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            crypto_detail = response.json()

            # Render the detail page with the cryptocurrency details
            return render(request, 'crypto_detail.html', {'crypto_detail': crypto_detail})

        else:
            return render(request, 'error.html', {'error_message': f"Failed to fetch data. Status code: {response.status_code}"})
    except Exception as e:
        return render(request, 'error.html', {'error_message': f"An error occurred: {str(e)}"})

def crypto_history_chart(request, crypto_id):
    # Define the API URL with the cryptocurrency ID and desired parameters
    api_url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': 30,  # You can adjust the number of days as needed
    }

    try:
        # Send a GET request to the API
        response = requests.get(api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the necessary data from the response
            prices = data['prices']
            # timestamps = [datetime.fromtimestamp((entry[0])/1000) for entry in prices]
            timestamps = [entry[0] for entry in prices]
            values = [entry[1] for entry in prices]

            # Render the historical chart template with the data
            return render(request, 'crypto_history_chart.html', {'crypto_id': crypto_id, 'timestamps': timestamps, 'values': values})

        else:
            return render(request, 'error.html', {'error_message': f"Failed to fetch data. Status code: {response.status_code}"})
    except Exception as e:
        return render(request, 'error.html', {'error_message': f"An error occurred: {str(e)}"})

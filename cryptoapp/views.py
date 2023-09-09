from django.core.paginator import Paginator
from django.shortcuts import render
import requests

def cryptocurrency_list(request):
    # Define the base URL of the CoinGecko API for fetching the list of cryptocurrencies
    base_url = "https://api.coingecko.com/api/v3/coins/list"

    try:
        # Send a GET request to fetch the list of cryptocurrency IDs
        response = requests.get(base_url)

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

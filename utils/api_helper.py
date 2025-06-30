import json
import os
from typing import Dict, Optional, Any
import requests
from requests.exceptions import RequestException
import logging

class APIHelper:
    """Base class for API interactions with common functionality."""
    
    def __init__(self):
        self.config = self._load_config()
        self.base_url = self.config["base_url"]
        self.endpoints = self.config["endpoints"]
        self.timeout = self.config.get("timeout", 30000)
        self.retry_count = self.config.get("retry_count", 3)
        self._setup_logging()
    
    def _setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def _load_config(self) -> Dict:
        """Load API configuration from JSON file."""
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                 "config", "api_config.json")
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Failed to load API config: {str(e)}")
    
    def _make_request(self, method: str, endpoint: str, 
                     data: Optional[Dict] = None, 
                     params: Optional[Dict] = None) -> requests.Response:
        """Make HTTP request with retry mechanism and error handling."""
        url = f"{self.base_url}{endpoint}"
        last_exception = None
        
        for attempt in range(self.retry_count):
            try:
                self.logger.info(f"Making {method} request to {url}")
                response = requests.request(
                    method=method,
                    url=url,
                    json=data,
                    params=params,
                    timeout=self.timeout/1000  # Convert to seconds
                )
                self.logger.info(f"Response status: {response.status_code}")
                return response
            
            except RequestException as e:
                last_exception = e
                self.logger.error(f"Request failed (attempt {attempt + 1}/{self.retry_count}): {str(e)}")
        
        raise last_exception or RequestException("Request failed after all retries")
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> requests.Response:
        """Make GET request."""
        return self._make_request("GET", endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> requests.Response:
        """Make POST request."""
        return self._make_request("POST", endpoint, data=data)
    
    def validate_response(self, response: requests.Response, 
                         expected_status: int = 200,
                         expected_response_code: Optional[int] = None) -> Dict[str, Any]:
        """Validate response status and content."""
        try:
            response_data = response.json()
        except ValueError:
            self.logger.error("Failed to parse response as JSON")
            raise
            
        assert response.status_code == expected_status, \
            f"Expected status code {expected_status} but got {response.status_code}"
            
        if expected_response_code is not None:
            assert response_data.get("responseCode") == expected_response_code, \
                f"Expected response code {expected_response_code} but got {response_data.get('responseCode')}"
                
        return response_data 
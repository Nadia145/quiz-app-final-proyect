import { useEffect } from 'react';
import axios from 'axios';


const MyComponent = () => {
  useEffect(() => {
    // Make the API request when the component mounts
    fetchData();
  }, []);

  const fetchData = () => {
    axios.get('http://127.0.0.1:5000/test')
      .then(response => {
        // Handle the response data
        console.log(response.data);
      })
      .catch(error => {
        // Handle any errors that occurred during the request
        console.error(error);
      });
  };

};

export default MyComponent;
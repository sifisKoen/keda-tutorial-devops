import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 16,
  duration: '300s',
};

export default function () {
  http.get('http://<your-service-url>/get_url'); // replace with your service URL.
  sleep(1);
}
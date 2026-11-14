# Dashboard queries

The four panels of the **Summit Cafe** dashboard (`http://localhost:3000/d/summit-cafe`). They follow the RED method (rate, errors, duration) plus one business metric.

## 1. Rate: requests per second

```promql
sum by (endpoint) (rate(http_requests_total[1m]))
```

How many requests per second the API answers, one line per endpoint, averaged over the last minute. A line that drops to zero means nobody is calling that endpoint.

## 2. Errors: share of 5xx

```promql
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))
```

The share of requests that ended in a server error (500 to 599) over the last 5 minutes. 0% is healthy; 0.05 shows as 5%, meaning one request in twenty failed.

## 3. Duration: p95

```promql
histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))
```

95% of the requests in the last 5 minutes were faster than this time. If it goes up, the slowest customers are waiting longer.

## 4. Business: orders per minute

```promql
sum(rate(orders_total[5m])) * 60
```

How many orders are created per minute, averaged over the last 5 minutes. Only orders that returned 201 count; rejected orders (400) do not.

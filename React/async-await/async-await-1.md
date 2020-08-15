We'll try to learn how async await works in react

Asynchronus functions return promises not values. It behaves non blocking way.

It provides clean and concise syntax that enables us to write less code to accomplish same result that you get from promises.

They can be paused using _await_

> Q-1: How do we write asynchronous function?

Well, You have to write just like normal function.

```javascript
const add = async (a, b) => {
  return a + b;
};

add(2, 3);
```

The importance of async await can be better understood if we use API call. Let's try this

We'll write 3 functions:

- Fetch data about currencies
- Fetch data about countries
- Output data

We're going to use some API for this purpose

1. [fixer API](https://fixer.io/). It'll provide us necessary data to calculate exchange rates between currencies.
2. [REST countries](http://restcountries.eu/). The REST Countries API provides a simple way of getting information about the world's nations via REST calls. These calls allow users to retrieve all available countries or to retrieve a given country's currency, capital city, calling code, region etc.

> Go to their website and collect free API upon registering.

---

Let's do the following tasks:

- create a **index.js** file
- type **npm init -y** in the terminal
- then install a dependency (axios) by typing **npm i axios** in the terminal
- Go to the _index.js_ file and declare these constants:

  ```js
  const FIXER_API_KEY = "your api key from (https://fixer.io/)";
  const FIXER_API = `http://data.fixer.io/api/latest?access_key=${FIXER_API_KEY}`;

  const REST_COUNTRIES_API = "https://restcountries.eu/rest/v2/currency";
  ```

Let's write our first function:

```js
const getExchangeRate = (fromCurrency, toCurrency) => {
  const { data } = axios.get(FIXER_API);

  console.log(data);
};

getExchangeRate("USD", "BDT");
```

We'll see the data in the console is _undefined_.

> Why data is undefined?

Because by default code executes in synchronous way. After calling the function the first line will execute

> const { data } = axios.get(FIXER_API);

the the second line will execute

> console.log(data);

But the first line will take some time to recieve data from API. Before fetching the data, second line already gets executed. So it has no value(undefined)

![one](/images/one.jpg "see my code")

**NB:** As I'm using _quokka_, a vscode extension, I can see the result immediately without going to the browser.

> So, how can we solve this problem?

We can solve this using _await_ keyword before the API call. also we need to use _async_ keyword because async-await comes in pair.

```js
const getExchangeRate = async (fromCurrency, toCurrency) => {
  const { data } = await axios.get(FIXER_API);

  console.log(data);
};

getExchangeRate("USD", "BDT");
```

Using _await_ keyword we're telling that please wait until I finish fetching the data, then after it finishes fetching the data, second line will execute.

![two](/images/two.jpg)

We only need currency from data. We can further destructure the _rates_ from data.

![rates](/images/rates.jpg)

```js
const getExchangeRate = async (fromCurrency, toCurrency) => {
  const {
    data: { rates },
  } = await axios.get(FIXER_API);

  console.log(rates);
};

getExchangeRate("USD", "BDT");
```

---

My full code is given in **index.js** file.

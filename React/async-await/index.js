import axios from "axios";

const FIXER_API_KEY = "dc3acf8e4256cb92e64c15a96b4d82c8";
const FIXER_API = `http://data.fixer.io/api/latest?access_key=${FIXER_API_KEY}`;

const REST_COUNTRIES_API = "https://restcountries.eu/rest/v2/currency";

const getExchangeRate = async (fromCurrency, toCurrency) => {
  try {
    const {
      data: { rates },
    } = await axios.get(FIXER_API);
    console.log(rates);

    const exchangeRate = rates[toCurrency] / rates[fromCurrency];

    return exchangeRate.toFixed(2);
  } catch (error) {
    throw new Error("Unable to get Currency");
  }
};

const getCountries = async (countryCode) => {
  const { data } = await axios.get(`${REST_COUNTRIES_API}/${countryCode}`);

  return data.map(({ name }) => name);
};

const converCurrency = async (fromCurrency, toCurrency, amount) => {
  fromCurrency = fromCurrency.toUpperCase();
  toCurrency = toCurrency.toUpperCase();

  // const countries = await getCountries(toCurrency);
  // const exchangeRate = await getExchangeRate(fromCurrency, toCurrency);
  /* 
    Above lines will take time for every await call. We can save time using
    the codes below.
  */

  const [countries, exchangeRate] = await Promise.all([
    getCountries(toCurrency),
    getExchangeRate(fromCurrency, toCurrency),
  ]);

  const convertedAmount = exchangeRate * amount;

  console.log(countries);
  console.log(exchangeRate);
  console.log(convertedAmount);
};

converCurrency("usd", "bdt", 200);

`React.memo()` is used to improve the performnce of our application by preventing re-rendering of pure components

> functional component by default re-renders every time its parent component renders.

We can prevent that by wrapping our target component with `React.memo()`

Let's create some file to try this.

> `index.js` file

```js
import React from "react";
import ReactDOM from "react-dom";

import App from "./App";

ReactDOM.render(<App />, document.querySelector("#root"));
```

> `App.js` file

```js
import React, { useState } from "react";
import Person from "./components/Person";

const App = () => {
  const [count, setCount] = useState(0);
  const [person] = useState({ name: "Jackie", age: 24 });
  return (
    <div>
      <Person person={person} />
      <h1>{count}</h1>
      <button onClick={() => setCount(count + 1)}>Add</button>
    </div>
  );
};

export default App;
```

> `Person.js` file without `React.memo()`

```js
import React from "react";

const Person = ({ person }) => {
  console.log("Person rendering");
  return (
    <div>
      <p>{person.name}</p>
      <p>{person.age}</p>
    </div>
  );
};

export default Person;
```

We'll see in the console that, _Person rendering_ when app loads for the first time.

But if we click the button, we'll see that the number of \*_Person rendering_ is equals to the number of _count_ value.

> `Person.js` file with `React.memo()`

```js
import React from "react";

const Person = ({ person }) => {
  console.log("Person rendering");
  return (
    <div>
      <p>{person.name}</p>
      <p>{person.age}</p>
    </div>
  );
};

export default React.memo(Person);
```

Now we'll see that it will be rendered only once when the application first rendered.

If we click the button we'll not see any additional _Person rendering_ in the console.

In this way we can optimize our application.

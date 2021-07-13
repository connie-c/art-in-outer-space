function App() {
  const [artpieces, setArtpieces] = React.useState({});
  const [fundingCart, setFundingCart] = React.useState({});
  const [loading, setLoading] = React.useState(false);

  React.useEffect(() => {
    setLoading(true);
    fetch("/api/artpieces")
      .then((response) => response.json())
      .then((artpieceData) => {
        setArtpieces(artpieceData);
        setLoading(false);
      });
  }, []);

  React.useEffect(() => {
    const previousCart = localStorage.getItem("fundingCart");
    if (previousCart) {
      setFundingCart(JSON.parse(previousCart));
    }
  }, []);

  React.useEffect(() => {
    localStorage.setItem("fundingCart", JSON.stringify(fundingCart));
  }, [fundingCart]);

  function addArtpieceToCart(artpieceId) {
    setFundingCart((currentFundingCart) => {
      const newFundingCart = Object.assign({}, currentFundingCart);

      if (newFundingCart[artpieceId]) {
        newFundingCart[artpieceId] += 1;
      } else {
        newFundingCart[artpieceId] = 1;
      }

      return newFundingCart;
    });
  }

  return (
    <ReactRouterDOM.BrowserRouter>
      <Navbar logo="/static/img/artpiece.jpeg" brand="Art in Outer Space">
        <ReactRouterDOM.NavLink
          to="/fund"
          activeClassName="navlink-active"
          className="nav-link"
        >
          Fund Art Pieces
        </ReactRouterDOM.NavLink>
        <ReactRouterDOM.NavLink
          to="/cart"
          activeClassName="navlink-active"
          className="nav-link"
        >
          Funding Cart
        </ReactRouterDOM.NavLink>
      </Navbar>

      <div className="container-fluid">
        <ReactRouterDOM.Route exact path="/">
          <Homepage />
        </ReactRouterDOM.Route>
        <ReactRouterDOM.Route exact path="/fund">
          {loading ? (
            <Loading />
          ) : (
            <AllArtpiecesPage artpieces={artpieces} addArtpieceToCart={addArtpieceToCart} />
          )}
        </ReactRouterDOM.Route>
        <ReactRouterDOM.Route exact path="/cart">
          {loading ? (
            <Loading />
          ) : (
            <FundingCartPage cart={fundingCart} artpieces={artpieces} />
          )}
        </ReactRouterDOM.Route>
      </div>
    </ReactRouterDOM.BrowserRouter>
  );
}

ReactDOM.render(<App />, document.querySelector("#root"));

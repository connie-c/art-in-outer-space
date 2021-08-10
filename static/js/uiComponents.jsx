function Homepage(props) {
  return (
    <div id="home-banner" className="row">
      <div className="col">
        <h1>Art in Outer Space</h1>
        <p className="lead">The ABSOLUTE FIRST EVER PLACE ONLINE FOR BILLIONAIRE ELITES to FUND AVANT-GARDE ART in OUTER SPACE.</p>
      </div>
    </div>
  );
}

function PageContainer(props) {
  const { children, className, title, ...rest } = props;
  return (
    <ReactRouterDOM.BrowserRouter>
      <h1>{title}</h1>
      <div {...rest} className={`row ${className || ""}`}>
        {children}
      </div>
    </ReactRouterDOM.BrowserRouter>
  );
}

function AllArtpiecesPage(props) {
  const { artpieces, addArtpieceToCart } = props;
  const artpieceCards = [];

  for (const artpiece of Object.values(artpieces)) {
    const artpieceCard = (
      <ArtpieceCard
        key={artpiece.artpiece_id}
        id={artpiece.artpiece_id}
        name={artpiece.name}
        imgUrl={artpiece.image_url}
        price={artpiece.price}
        handleAddToCart={addArtpieceToCart}
      />
    );

    artpieceCards.push(artpieceCard);
  }

  return (
    <PageContainer title="All Art Pieces" id="funding">
      <div className="col-12 col-md-9 d-flex flex-wrap">{artpieceCards}</div>
    </PageContainer>
  );
}

function FundingCartPage(props) {
  const { cart, artpieces } = props;
  const tableData = [];
  let totalCost = 0;
  for (const artpieceId in cart) {
    const currentArtpiece = artpieces[artpieceId];
    const artpieceCost = cart[artpieceId] * currentArtpiece.price;
    totalCost += artpieceCost;
    tableData.push(
      <tr key={artpieceId}>
        <td>{currentArtpiece.name}</td>
        <td>{cart[artpieceId]}</td>
        <td>${artpieceCost.toFixed(2)} BITCOINS</td>
      </tr>
    );
  }
  return (
    <PageContainer title="Funding Cart" id="fundingCart">
      <div className="col-6">
        <table className="table">
          <thead>
            <tr>
              <th>Artpiece</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>{tableData}</tbody>
        </table>
        <p className="lead">Total: ${totalCost.toFixed(2)} BITCOINS</p>
      </div>
    </PageContainer>
  );
}

function Navbar(props) {
  const { logo, brand, children, className } = props;

  const navLinks = children.map((el, i) => {
    return (
      <div key={i} className="nav-item">
        {el}
      </div>
    );
  });

  return (
    <nav className={`navbar ${className || ""}`}>
      <ReactRouterDOM.Link
        to="/"
        className="havbar-brand d-flex justify-content-center"
      >
        <img src={logo} height="30" />
        <span>{brand}</span>
      </ReactRouterDOM.Link>

      <section className="d-flex justify-content-center">{navLinks}</section>
    </nav>
  );
}

function ArtpieceCard(props) {
  const { id, name, imgUrl, price, handleAddToCart } = props;

  return (
    <div className="card artpiece-card">
      <ReactRouterDOM.Link to={`/fund/${id}`}>
        <img src={imgUrl} className="card-img-top" />
      </ReactRouterDOM.Link>
      <div className="card-body">
        <h5 className="card-title">
          <ReactRouterDOM.Link to={`/fund/${id} BITCOINS`}>{name}</ReactRouterDOM.Link>
        </h5>
      </div>
      <div className="card-body pt-0 container-fluid">
        <div className="row">
          <div className="col-12 col-lg-6">
            <span className="lead price d-inline-block">
              ${price.toFixed(2)} BITCOINS
            </span>
          </div>
          <div className="col-12 col-lg-6">
            <button
              className="btn btn-sm btn-success d-inline-block"
              onClick={() => handleAddToCart(id)}
            >
              FULLY FUND
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

function Loading() {
  return (
    <div className="loading-box">
      <img src="https://lh3.googleusercontent.com/-2Gnwevre-pY/YQ6D9v0I9eI/AAAAAAAAAfQ/M-nmBdDU5uctEiKVvMjfq-PJPXMb4hi7QCNcBGAsYHQ/w640-h320/artpiece-loading.jpg"/>
      <div>3...2...1...BLAST OFF!!!!!</div>
    </div>
  );
}
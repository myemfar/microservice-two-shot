function HatsList(props) {
    return (
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Fabric</th>
            <th>Style</th>
            <th>Color</th>
            <th>Picture</th>
            <th>Location</th>
          </tr>
        </thead>
        <tbody>
          {props.hats.map(hat => {
            return (
              <tr key={hat.id}>
                <td>{ hat.fabric }</td>
                <td>{ hat.style_name }</td>
                <td>{ hat.color }</td>
                <td><img src={hat.picture} alt="..." width="300" /></td>
                <td>{ hat.location.closet_name }</td>
                <td>details</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }

  export default HatsList;
// import React from 'react';

// function HatsColumn(props) {
// return (
//     <div className="col">
//     {props.hats.map(hat => {
//         return (
//         <div key={hat.id} className="card mb-3 shadow">
//             <img src={hat.picture} className="card-img-top" />
//             <div className="card-body">
//             <h5 className="card-title">{hat.fabric}</h5>
//             <h6 className="card-subtitle mb-2 text-muted">
//                 {hat.color}
//             </h6>
//             <p className="card-text">
//                 {hat.location.closet_name}
//             </p>
//             </div>
//         </div>
//         );
//     })}
//     </div>
// );
// }

// class HatsList extends React.Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//         hatsColumns: [[], [], []],
//         };
//     }

//     async componentDidMount() {
//         const url = 'http://localhost:8090/api/hats/';

//         try {
//         const response = await fetch(url);
//         if (response.ok) {
//             // Get the list of conferences
//             const data = await response.json();

//             // Create a list of for all the requests and
//             // add all of the requests to it
//             const requests = [];
//             for (let hat of data.hats) {
//             const detailUrl = `http://localhost:8090/api/hats/${hat.id}`;
//             requests.push(fetch(detailUrl));
//             }

//             // Wait for all of the requests to finish
//             // simultaneously
//             const responses = await Promise.all(requests);

//             // Set up the "columns" to put the conference
//             // information into
//             const hatColumns = [[], [], []];

//             // Loop over the conference detail responses and add
//             // each to to the proper "column" if the response is
//             // ok
//             let i = 0;
//             for (const hatResponse of responses) {
//             if (hatResponse.ok) {
//                 const details = await hatResponse.json();
//                 hatColumns[i].push(details);
//                 i = i + 1;
//                 if (i > 2) {
//                 i = 0;
//                 }
//             } else {
//                 console.error(hatResponse);
//             }
//             }

//             // Set the state to the new list of three lists of
//             // conferences
//             this.setState({hatColumns: hatColumns});
//         }
//         } catch (e) {
//         console.error(e);
//         }
//     }

//     render() {
//         return (
//         <>
//             <div className="container">
//             <h2>Hats</h2>
//             <div className="row">
//                 {this.state.hatColumns.map((hatList, index) => {
//                 return (
//                     <HatsColumn key={index} list={hatList} />
//                 );
//                 })}
//             </div>
//             </div>
//         </>
//         );
//     }
// }

// export default HatsList;

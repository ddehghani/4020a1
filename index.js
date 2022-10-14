//https://developer.mozilla.org/en-US/docs/Web/Guide/Parsing_and_serializing_XML
// loading the document

const xhr = new XMLHttpRequest();
var titles;

xhr.onload = () => {
  console.log(xhr.responseXML.documentElement.nodeName); // document can be parsed here
  titles = xhr.responseXML.getElementsByTagName("ArticleTitle")
  console.log(titles);
  //still need to remove the actual tags from the list items (should leave only )
  console.log(titles[0])
}

xhr.onerror = () => {
  console.log("Error while getting XML."); 
}

xhr.open("GET", "http://localhost:80/4020a1/4020a1-datasets.xml",false);
  //xhr.responseType = "document";
  xhr.send();

console.log(titles[7]);

  // response xml, check document docs on how to output it, may not need to serialize

// var or const?


  // serialize
  // const serializer = new XMLSerializer();
  // const xmlStr = serializer.serializeToString(xhr.responseXML);

  
//------------------------------

// const doc = "4020a1-datasets.xml"
// const serializer = new XMLSerializer();
// const xmlStr = serializer.serializeToString(doc);

// parser = new DOMParser();
// xmlDoc = parser.parseFromString(xmlStr,"text/xml");

// var titles = xmlDoc.getElementsByTagName("ArticleTitle")[0].nodeValue;

// console.log(titles);


//----------------------------------------------

// document.getElementById("demo").innerHTML =
// xmlDoc.getElementsByTagName("title")[0].childNodes[0].nodeValue;
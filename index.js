//https://developer.mozilla.org/en-US/docs/Web/Guide/Parsing_and_serializing_XML
// loading the document
function getTitlesObject() {
  const xhr = new XMLHttpRequest();
  var titles;

  xhr.onload = () => {
    console.log(xhr.responseXML.documentElement.nodeName); // document can be parsed here
    titles = xhr.responseXML.getElementsByTagName("ArticleTitle") // titles is an HTMLCollection object
    //console.log(titles);
    //still need to remove the actual tags from the list items (should leave only )
    console.log(titles[0])
  }

  xhr.onerror = () => {
    console.log("Error while getting XML.");
  }

  xhr.open("GET", "http://localhost:80/4020a1/4020a1-datasets.xml",false); // set async to false to allow response.xml to be accessed outside of onload()
    xhr.send();

  //console.log(titles[7]);

  return titles;
  
  
}

function isolateInnerHTMLFieldsFromTitles(titlesObject) { // titles is an HTMLCollection object
  //test length function on titlesObject - check 
  console.log(titlesObject.length)

  //Loop through and extract innerhtml between all <ArticleTitle> tags 
  var i = 0, len = titlesObject.length;
  var titlesArray = []
  while (i < len) {
      // your code
      titlesArray[i] = titlesObject[i].innerHTML;
      
      i++ //iterator
  }
  console.log(titlesArray);
  return titlesArray;
}

//Check 
var firstTitle = isolateInnerHTMLFieldsFromTitles(getTitlesObject())[0];
console.log(firstTitle);
//Run functions




console.log("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed"+"&term="+firstTitle);
var titlesArrayInput = isolateInnerHTMLFieldsFromTitles(getTitlesObject());

function getPMIDsFromAPI (inputArray) {
  const xhr = new XMLHttpRequest();
  var pmids;

  xhr.onload = () => {
    pmids = xhr.responseXML;
    console.log(xhr.responseXML)
    console.log(xhr.responseXML.getElementsByTagName("PMID")[0]);
    console.log(pmids[0]); // check first pmid to see if results were correct
  }

  xhr.onerror = () => {
    console.log("Error while getting XML.");
  }

  // press ctrl+k+c to comment something out in vscode
  // var i = 0, len = titlesObject.length;
  // var titlesArray = [];
  console.log("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed"+"term"+firstTitle);
  // while (i < len) {
      // your code
      xhr.open("GET", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%22John%20Snow%20and%20modern-day%20environmental%20epidemiology%22&field=title",false); //
  //hr.open("GET", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed"+"&term="+firstTitle,false); // set async to false to allow response.xml to be accessed outside of onload()
  xhr.send();
  //    i++ //iterator
  // }

  //console.log(titles[7]);

  return pmids;
}

getPMIDsFromAPI(titlesArrayInput); 
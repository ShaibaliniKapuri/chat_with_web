graph [
  directed 1
  node [
    id 0
    label "Langchain_Huggingface"
  ]
  node [
    id 1
    label "Hugging Face"
  ]
  node [
    id 2
    label "Langchain"
  ]
  node [
    id 3
    label "Llms"
  ]
  node [
    id 4
    label "Huggingfacepipeline"
  ]
  node [
    id 5
    label "Huggingfaceendpoint"
  ]
  node [
    id 6
    label "Chathuggingface"
  ]
  node [
    id 7
    label "Huggingfaceembeddings"
  ]
  node [
    id 8
    label "Huggingfaceendpointembeddings"
  ]
  edge [
    source 0
    target 2
    relation "PARTNER"
  ]
  edge [
    source 0
    target 1
    relation "PARTNER"
  ]
  edge [
    source 0
    target 4
    relation "UTILIZES"
  ]
  edge [
    source 0
    target 5
    relation "UTILIZES"
  ]
  edge [
    source 0
    target 7
    relation "UTILIZES"
  ]
  edge [
    source 4
    target 5
    relation "USES"
  ]
  edge [
    source 5
    target 8
    relation "SIMILAR"
  ]
  edge [
    source 6
    target 5
    relation "WRAPS"
  ]
  edge [
    source 6
    target 8
    relation "WRAPS"
  ]
  edge [
    source 7
    target 8
    relation "SIMILAR"
  ]
  edge [
    source 7
    target 5
    relation "UTILIZES"
  ]
]

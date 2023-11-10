import re
import requests


# Criado por Levi 62425
contador = 1
def Chamado():
    qualquerjson = { 
            "Descricao":"Nova Politica de Firewall (Auto)",
            "ReportadoPor":"1008229",
            "PessoaAfetada":"1008229",
            "GrupoProprietario":"GRUPO02",
            "GrupoConveniencia":"",
            "Conveniencia":"",
            "Site":"SPMENOS",
            "Org":"PMENOS",
            "Template":"FIREWALL.PO2",
            "GrupoPessoaAtribuida":"GRUPO02",
            "SistemExterno":"SERVICECATALOG",
            "CriadoPor":"1008229",
            "Classificacao":"FIREWALL.PO2",
            "PmscItemNumero":"FIREWALL.PO2",
            "PmscResumo":"Nova Politica de Firewall (Auto)",
            "PmscItemSet":"ISET",
            "PmscQuantidade":1,
            "Classe":"SS",
            "TipoOcorrencia":"",
            "Filial":"",
            "Observacao":"Nova Politica de Firewall (Auto)",
            "Anexos": [],
            "Atributos": [ 
                    { 
                            "Chave":"DETALHES",
                            "Valor":'Criação do grupo SAP_PROD para o Analista Wilson',
                            "Ordem":1,
                            "Tipo":"STRING"
                    },
                    { 
                            "Chave":"TRATRDS",
                            "Valor":'Serviço já feito, RDS para registro',
                            "Ordem":2,
                            "Tipo":"STRING"
                    }
            ]
    }

    #Submento o POST à API
    r = requests.post('http://k8s.pmenos.com.br/centralchamados/api/Chamado', json=qualquerjson)
    print(r)
    print(r.text)

while contador <= 31:
    Chamado()
    contador = contador + 1
    

    



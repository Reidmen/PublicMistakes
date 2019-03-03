#!/usr/bin python3
# Created by Reidmen Arostica reidmen@dim.uchile.cl
# version 1.0 - 06/01/2019
# Packages necessary for the script
import scipy.io as sio
import numpy as np
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.etree import ElementTree
import xml.etree.cElementTree as CTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    #rough_string = ElementTree.tostring(elem, 'utf-8')
    rough_string = ElementTree.tostring(elem, encoding='UTF-8',
                                        method='xml')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def XMLSubDomains(elems, filename):
    """
    Creates a filename XML file from nodes and elems mesh data
    Suitable for usage in FEniCS software
    """
    # First, create the XML file structure
    xml_dolfin = Element('dolfin')
    xml_dolfin.set('xmlns:dolfin','reidmen.github.io/RevealPresentation')
    comment = Comment('v.0.0 Implemented by: Reidmen Arostica 2018')
    xml_dolfin.append(comment)
    # Create mesh element and atributes
    xml_mesh = SubElement(xml_dolfin, 'mesh_function')
    xml_mesh.set('type', 'int')
    xml_mesh.set('dim', '3')
    
    # Then, define cells sub-elements
    num_elems = elems.shape[0]
    # OBS: the +1 since in FEniCS the size is [0, NumNodes)
    xml_mesh.set('size', str(num_elems)) # Set the number of elements
    
    # Iterate over each elem (tetrahedra) to assing the indexes
    for elem_id in range(num_elems):
        xml_tetra = SubElement(xml_mesh, 'entity')
        xml_tetra.set('index',  str(elem_id))
        # Assign tag associated to subdomain --> (matrix or porous)
        tag = int(1 if elems[elem_id][4] > 1 else 0)
        xml_tetra.set('value', str(tag))
    
    # DEBUG!: Print sample and generate file
    #print(prettify(xml_dolfin))
    tree = CTree.ElementTree(xml_dolfin)
    tree.write(str(filename))
    # Return empty
    return


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        print("Required just input and output filenames")
    else:
        #filename = 'Cortical3dsc04Mesh1200SFill-CGALMesh'
        #mesh_data = sio.loadmat('FromOctave/FromScaled/'+filename+'.mat')
        filename = sys.argv[0]
        mesh_data = sio.loadmat(filename+'.mat')
        # Assign nodes, elems, faces
        nodes = mesh_data['nodefill']
        elems = mesh_data['elemfill']
        faces = mesh_data['facefill']
        # points var. has format (num. cc, [X, Y, Z])
        points = mesh_data['points']
        print("""Size of Nodes array: {}
        Size of Elems array: {}
        Size of Faces array: {} """.format(nodes.shape, elems.shape, faces.shape))
        print("Creating mesh ...")
        XMLSubDomains(elems, filename+'_subdomains.xml')

 

#XMLSubDomains(elems[0:7], 'Domains/ExampleSub.xml')
#XMLSubDomains(elems, 'Domains/'+filename+'_subdomains.xml')
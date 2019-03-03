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
import sys
import os

"""
XYZtoXMLMesh creates from a .mat file of nodes, elements, and faces.
To use:
python3 XYZtoXMLMesh.py 'filename' 
"""

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    #rough_string = ElementTree.tostring(elem, 'utf-8')
    rough_string = ElementTree.tostring(elem, encoding='UTF-8',
                                        method='xml')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def XMLMesh(nodes, elems, filename):
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
    xml_mesh = SubElement(xml_dolfin, 'mesh')
    xml_mesh.set('celltype', 'tetrahedron')
    xml_mesh.set('dim', '3')
    # Then, define vertices and cells sub-elements
    num_nodes = nodes.shape[0]
    num_elems = elems.shape[0]
    
    # OBS: the +1 since in FEniCS the size is [0, NumNodes)
    xml_vertices = SubElement(xml_mesh, 'vertices')
    xml_vertices.set('size', str(num_nodes)) # Set the number of nodes
    xml_cells = SubElement(xml_mesh, 'cells')
    xml_cells.set('size', str(num_elems)) # Set the number of elements
    
    # Iterate over each node to obtain the vertices

    for node_id in range(num_nodes):
        xml_vertex = SubElement(xml_vertices, 'vertex')
        xml_vertex.set('index', str(node_id))
        # Add x,y,z values at node id
        xml_vertex.set('x', '{:0.5e}'.format(nodes[node_id][0]))
        xml_vertex.set('y', '{:0.5e}'.format(nodes[node_id][1]))
        xml_vertex.set('z', '{:0.5e}'.format(nodes[node_id][2]))
        
    # Iterate over each element to assing the tetrahedron
    for elem_id in range(num_elems):
        xml_tetra = SubElement(xml_cells, 'tetrahedron')
        xml_tetra.set('index',  str(elem_id))
        # Assign each vertex of the tetrahedra
        v_0 = int(elems[elem_id][0]) - 1
        v_1 = int(elems[elem_id][1]) - 1
        v_2 = int(elems[elem_id][2]) - 1
        v_3 = int(elems[elem_id][3]) - 1
        xml_tetra.set('v0', str(v_0))
        xml_tetra.set('v1', str(v_1))
        xml_tetra.set('v2', str(v_2))
        xml_tetra.set('v3', str(v_3))
    
    # DEBUG!: Print sample and generate file
    #print(prettify(xml_dolfin))
    tree = CTree.ElementTree(xml_dolfin)
    #tree = ElementTree.ElementTree(xml_dolfin)
    tree.write(str(filename), encoding='UTF-8', xml_declaration=True)
    # Return empty
    return 

if __name__ == "__main__":

    if len(sys.argv) > 2:
        print("Required just input filename!")
        print("Requires filename without format specification (.mat)")
    else:
        #filename = 'Cortical3dsc04Mesh1200SFill-CGALMesh'
        #mesh_data = sio.loadmat('FromOctave/FromScaled/'+filename+'.mat')
        cwd = os.getcwd() # Obtain current working directory
        filename = sys.argv[1]
        mesh_data = sio.loadmat(cwd+'/'+filename+'.mat')
        # Assign nodes, elems, faces
        nodes = mesh_data['node']
        elems = mesh_data['elem']
        faces = mesh_data['face']
        # points var. has format (num. cc, [X, Y, Z])
        print("""Size of Nodes array: {}
        Size of Elems array: {}
        Size of Faces array: {} """.format(nodes.shape, elems.shape, faces.shape))
        print("Creating mesh ...")
        XMLMesh(nodes, elems, filename+'.xml')


#XMLMesh(nodes[0:10], elems[0:7], 'Domains/Example.xml')
#XMLMesh(nodes, elems, 'Domains/'+filename+'.xml')
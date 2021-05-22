#version 330 

in vec3 fPosition; 

in vec2 fTexCoord; 

in vec3 fNormal; 

in vec3 fTangent; 

in vec3 fBitangent; 

layout(location = 0) out vec4 fragColor; 


void main(){

fragColor= vec4(1);

}
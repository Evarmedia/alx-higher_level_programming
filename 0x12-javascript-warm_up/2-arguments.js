#!/usr/bin/node

const numberOfArgs = process.argv.length;

if (numberOfArgs === 2){
	console.log("No Argument");
}else if (numberOfArgs > 2){
	console.log('Argument found')
}

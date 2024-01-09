#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
	for ( i = 0; i < x; i++) {
		theFunction();
	}
}

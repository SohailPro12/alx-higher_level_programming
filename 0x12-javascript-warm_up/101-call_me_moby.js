#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
	for ( i = 1; i < x; i++) {
		theFunction();
	}
}

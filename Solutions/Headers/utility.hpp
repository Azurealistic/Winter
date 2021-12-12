#pragma once

// This header is used to consolidate all of the utility functions I might need throughout AoC.
#include <vector>
#include <string_view>

namespace Utility {
	// This function can split a given input string_view into a vector of string_view based on the delimiter.
	std::vector<std::string_view> split(std::string_view input, char delimiter) {
		std::vector<std::string_view> result;
		std::size_t pos = 0;
		while((pos = input.find(delimiter)) != std::string_view::npos) {
			result.push_back(input.substr(0, pos));
			input.remove_prefix(pos + 1);
		}
		result.push_back(input);
		return result;
	}
}
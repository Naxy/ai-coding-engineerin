package amount

import (
	"errors"
	"math"
)

var ErrInvalidInput = errors.New("price and quantity must be non-negative")

func Payable(unitPriceCents int64, quantity int64) (int64, error) {
	if unitPriceCents < 0 || quantity < 0 {
		return 0, ErrInvalidInput
	}
	if quantity != 0 && unitPriceCents > math.MaxInt64/quantity {
		return 0, errors.New("amount overflow")
	}
	return unitPriceCents * quantity, nil
}
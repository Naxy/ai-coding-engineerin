package amount

import (
	"errors"
	"testing"
)

func TestPayable(t *testing.T) {
	got, err := Payable(335, 3)
	if err != nil || got != 1005 {
		t.Fatalf("Payable() = %d, %v; want 1005, nil", got, err)
	}
}

func TestPayableRejectsNegative(t *testing.T) {
	_, err := Payable(100, -1)
	if !errors.Is(err, ErrInvalidInput) {
		t.Fatalf("want ErrInvalidInput, got %v", err)
	}
}

func TestPayableOverflow(t *testing.T) {
	_, err := Payable(2, int64(^uint64(0)>>1))
	if err == nil {
		t.Fatal("want overflow error")
	}
}
package dev.aicoding;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class OrderAmountService {
    public BigDecimal calculatePayable(BigDecimal unitPrice, int quantity) {
        if (unitPrice == null || unitPrice.signum() < 0) {
            throw new IllegalArgumentException("unitPrice must be non-negative");
        }
        if (quantity < 0) {
            throw new IllegalArgumentException("quantity must be non-negative");
        }
        return unitPrice.multiply(BigDecimal.valueOf(quantity))
                .setScale(2, RoundingMode.HALF_UP);
    }
}
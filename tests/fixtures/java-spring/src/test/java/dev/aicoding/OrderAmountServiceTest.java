package dev.aicoding;

import static org.junit.jupiter.api.Assertions.*;
import java.math.BigDecimal;
import org.junit.jupiter.api.Test;

class OrderAmountServiceTest {
    private final OrderAmountService service = new OrderAmountService();

    @Test void calculatesAndRoundsMoney() {
        assertEquals(new BigDecimal("10.01"),
                service.calculatePayable(new BigDecimal("3.336"), 3));
    }

    @Test void rejectsNegativeQuantity() {
        assertThrows(IllegalArgumentException.class,
                () -> service.calculatePayable(new BigDecimal("1.00"), -1));
    }

    @Test void rejectsNullPrice() {
        assertThrows(IllegalArgumentException.class,
                () -> service.calculatePayable(null, 1));
    }
}
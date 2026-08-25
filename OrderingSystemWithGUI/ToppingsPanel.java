import javax.swing.*;
import java.awt.*;


/**
 * This class designs panels for topping and has a method for retrieving the total cost of toppings selected.
 * 
 * @author sailaborn
 * @version 1.0
 * @since 20 April 2026
 */
public class ToppingsPanel  extends JPanel{
	protected JCheckBox mushroom = new JCheckBox("Mushroom (+$0.25)");
	protected JCheckBox pepperoni = new JCheckBox("Pepperoni (+$0.35)");
	protected JCheckBox jalapenos = new JCheckBox("Jalapenos (+$0.45)");

public ToppingsPanel() {
    setLayout(new BorderLayout());
    JLabel label = new JLabel("Toppings", SwingConstants.CENTER);
    
    JPanel cbPanel = new JPanel(); 
    cbPanel.add(pepperoni);
    cbPanel.add(jalapenos);
    cbPanel.add(mushroom);
    
    add(label, BorderLayout.NORTH);
    add(cbPanel, BorderLayout.CENTER);
}
/** This method gets the total cost of toppings selected */
	public double getToppingCost() {
		add(new JLabel("Toppings"), BorderLayout.NORTH);
		double toppingCost = 0;
		if (mushroom.isSelected()) toppingCost += 0.25;
		if (pepperoni.isSelected()) toppingCost += 0.35;
		if (jalapenos.isSelected()) toppingCost += 0.45;
		return toppingCost;
	}
}
	
	
	



